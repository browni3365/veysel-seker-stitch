#!/usr/bin/env python3
"""VEYSEL ŞEKER Pattern Studio — local GUI (tkinter, no license)."""

from __future__ import annotations

import sys
import threading
import traceback
from pathlib import Path
from tkinter import BOTH, END, LEFT, RIGHT, StringVar, Tk, filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from app.pipeline import Pipeline  # noqa: E402
from app.settings_manager import SettingsManager  # noqa: E402


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("VEYSEL ŞEKER  ·  Cross Stitch Studio")
        self.geometry("780x620")
        self.settings = SettingsManager()
        self.image_path: Path | None = None

        pad = {"padx": 10, "pady": 6}
        frm = ttk.Frame(self)
        frm.pack(fill=BOTH, expand=True, **pad)

        ttk.Label(frm, text="Görsel / Image").grid(row=0, column=0, sticky="w")
        self.path_var = StringVar()
        ttk.Entry(frm, textvariable=self.path_var, width=62).grid(row=0, column=1, sticky="we")
        ttk.Button(frm, text="Seç…", command=self.pick).grid(row=0, column=2)

        ttk.Label(frm, text="Başlık / Title").grid(row=1, column=0, sticky="w")
        self.title_var = StringVar(value="Midnight Owl")
        ttk.Entry(frm, textvariable=self.title_var, width=62).grid(row=1, column=1, columnspan=2, sticky="we")

        ttk.Label(frm, text="Genişlik (stitches)").grid(row=2, column=0, sticky="w")
        self.w_var = StringVar(value=str(self.settings.get("default_width", 80)))
        ttk.Entry(frm, textvariable=self.w_var, width=10).grid(row=2, column=1, sticky="w")

        ttk.Label(frm, text="Maks. DMC renk").grid(row=3, column=0, sticky="w")
        self.c_var = StringVar(value=str(self.settings.get("default_max_colors", 36)))
        ttk.Entry(frm, textvariable=self.c_var, width=10).grid(row=3, column=1, sticky="w")

        ttk.Label(frm, text="Aida count").grid(row=4, column=0, sticky="w")
        self.a_var = StringVar(value=str(self.settings.get("default_aida", 14)))
        ttk.Entry(frm, textvariable=self.a_var, width=10).grid(row=4, column=1, sticky="w")

        btns = ttk.Frame(frm)
        btns.grid(row=5, column=0, columnspan=3, sticky="w", pady=10)
        ttk.Button(btns, text="Üret / Generate", command=self.generate).pack(side=LEFT, padx=4)
        ttk.Button(btns, text="Çıkış", command=self.destroy).pack(side=LEFT, padx=4)

        self.log = ScrolledText(frm, height=22, font=("DejaVu Sans Mono", 10))
        self.log.grid(row=6, column=0, columnspan=3, sticky="nsew")
        frm.rowconfigure(6, weight=1)
        frm.columnconfigure(1, weight=1)
        self._log("Yerel stüdyo hazır. Lisans yok — çıktılar senindir.\n")

    def pick(self) -> None:
        p = filedialog.askopenfilename(
            title="Görsel seç",
            filetypes=[("Images", "*.png *.jpg *.jpeg *.webp *.bmp"), ("All", "*.*")],
        )
        if p:
            self.image_path = Path(p)
            self.path_var.set(p)

    def _log(self, msg: str) -> None:
        self.log.insert(END, msg)
        self.log.see(END)

    def generate(self) -> None:
        path = self.image_path or (Path(self.path_var.get()) if self.path_var.get() else None)
        if not path or not path.exists():
            messagebox.showerror("Eksik", "Lütfen bir görsel seçin.")
            return
        title = self.title_var.get().strip() or path.stem
        try:
            width = int(self.w_var.get())
            colors = int(self.c_var.get())
            aida = int(self.a_var.get())
        except ValueError:
            messagebox.showerror("Hata", "Sayısal alanları kontrol edin.")
            return
        self.settings.set("default_width", width)
        self.settings.set("default_max_colors", colors)
        self.settings.set("default_aida", aida)

        def work() -> None:
            try:
                self._log(f"\n→ {title}  {width}w  {colors}c  Aida {aida}\n")
                pipe = Pipeline(ROOT / self.settings.get("output_root", "output"))
                res = pipe.run(path, title=title, width=width, max_colors=colors, aida=aida)
                self._log(res.qa_text + "\n")
                self._log(f"Klasör: {res.folder}\n")
                for f in res.files:
                    self._log(f"  {f.name}\n")
                self._log("Bitti.\n")
            except Exception:
                self._log(traceback.format_exc())

        threading.Thread(target=work, daemon=True).start()


def main() -> int:
    App().mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
