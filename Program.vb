Imports System
Module Program
    Sub Main(args As String())
        Dim N As Integer
        Dim Z As Integer = 1
        Dim i As Integer = 0
        Do
            i = i + 1

            Console.WriteLine("����� {0}� ���������", i)
            N = Console.ReadLine()
            Z = Z * N
            Console.WriteLine("������������ ={0}", Z)

        Loop Until N = 1
    End Sub
End Module
