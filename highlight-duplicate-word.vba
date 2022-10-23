Option Explicit



Sub Sample()

    Dim MyArray() As String

    Dim n As Long, i As Long

    Dim Col As New Collection

    Dim itm



    n = 0

    '~~> Get all the sentences from the word document in an array

    For i = 1 To ActiveDocument.Sentences.Count

        n = n + 1

        ReDim Preserve MyArray(n)

        MyArray(n) = Trim(ActiveDocument.Sentences(i).Text)

    Next



    '~~> Sort the array

    SortArray MyArray, 0, UBound(MyArray)



    '~~> Extract Duplicates

    For i = 1 To UBound(MyArray)

        If i = UBound(MyArray) Then Exit For

        If InStr(1, MyArray(i + 1), MyArray(i), vbTextCompare) Then

            On Error Resume Next

            Col.Add MyArray(i), """" & MyArray(i) & """"

            On Error GoTo 0

        End If

    Next i



    '~~> Highlight duplicates

    For Each itm In Col

        Selection.Find.ClearFormatting

        Selection.HomeKey wdStory, wdMove

        Selection.Find.Execute itm

        Do Until Selection.Find.Found = False

            Selection.Range.HighlightColorIndex = wdPink

            Selection.Find.Execute

        Loop

    Next

End Sub



'~~> Sort the array

Public Sub SortArray(vArray As Variant, i As Long, j As Long)

  Dim tmp As Variant, tmpSwap As Variant

  Dim ii As Long, jj As Long



  ii = i: jj = j: tmp = vArray((i + j) \ 2)



  While (ii <= jj)

     While (vArray(ii) < tmp And ii < j)

        ii = ii + 1

     Wend

     While (tmp < vArray(jj) And jj > i)

        jj = jj - 1

     Wend

     If (ii <= jj) Then

        tmpSwap = vArray(ii)

        vArray(ii) = vArray(jj): vArray(jj) = tmpSwap

        ii = ii + 1: jj = jj - 1

     End If

  Wend

  If (i < jj) Then SortArray vArray, i, jj

  If (ii < j) Then SortArray vArray, ii, j

End Sub
