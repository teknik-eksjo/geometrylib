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

  pyvenv install -r requirements.txt venv

Aktivera den virtella körmiljön:

.. code-block::

  . venv/bin/activate

Om du använder Windows:

.. code-block::

  venv/Script/activate.bat

För att köra enhetstesterna kan

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



.. _unittest: https://docs.python.org/3.5/library/unittest.html
.. _coverage.py: https://coverage.readthedocs.org/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _code coverage: https://en.wikipedia.org/wiki/Code_coverage
