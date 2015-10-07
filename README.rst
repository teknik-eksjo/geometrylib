geometrylib
===========

Detta är ett projekt som introducerar enhetstester och Sphinx. För
enhetstesterna använder vi standardmodulen unittest_ tillsammans med
coverage.py_ för att få ett mått på `code coverage`_.
Dokumentationen skapar vi med hjälp av Sphinx_.

Innan du börjar
---------------
Skapa den virtuella körmiljön med de paket som behövs.

.. code-block::

  pyvenv venv

Aktivera den virtella körmiljön:

.. code-block::

  . venv/bin/activate

Om du använder Windows:

.. code-block::

  venv/Script/activate.bat

Installera de paket som behövs för uppgiften:

.. code-block::

  pip install -r requirements.txt

Uppgiften
---------

1.  Skriv tester för alla metoder i klassen Triangle och funktionerna i modulen
    utils. Använd olika assert-metoder där det är lämpligt. Tänk lite extra på
    vilka tester som behövs och vilka som bidrar med något intressant. Finns
    det ett test för något som ska fungera och ett test för något som inte ska
    fungera? Finns det några gränser som kan vara intressanta att testa?

2.  Skriv kod som klarar alla testerna. Se till att du får 100% code coverage,
    det kan betyda att du måste återvända och ändra eller komplettera dina
    tester.

    För att köra enhetstesterna med coverage.py kan du använda följande kommando

    .. code-block::

      python manage.py test --coverage

3.  Generera dokumentation med Sphinx. Använd :code:`sphinx-quickstart` för att
    snabbt komma igång. Dokumentationen ska bestå av tre delar;

    :code:`api.rst`
      Använd autodoc för att dokumentera geometrylib.
    :code:`tutorial.rst`
      Utgå från texten i filen :code:`tutorial.txt` och lägg till den markup
      som saknas.
    :code:`guide.rst`.
      Utgå från texten i filen :code:`guide.txt` och lägg till den markup som
      saknas.

    För att bygga html-versionen av dokumentationen kör du följande i mappen
    :code:`docs`.

    .. code-block::

      make html

    För att testa att de kodexempel som finns i dokumentationen fungerar kan
    du köra :code:`make doctest`. Ibland trilskas referenser och index och då
    kan man behöva köra :code:`make clean` innan :code:`make html`.

    Kom ihåg att bara filer som refereras från :code:`ìndex.rst` genereras
    när du kör :code:`make html`.

.. _unittest: https://docs.python.org/3.5/library/unittest.html
.. _coverage.py: https://coverage.readthedocs.org/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _code coverage: https://en.wikipedia.org/wiki/Code_coverage
