/*Проверка свойства дерева поиска
Проверить, является ли данное двоичное дерево деревом поиска.
Вход. Двоичное дерево.
Выход. Проверить, является ли оно корректным деревом поиска: верно ли, что для любой вершины дерева её ключ больше всех ключей в левом поддереве данной вершины и меньше всех ключей в правом поддереве.*/

using System;
using System.Linq;
using System.Collections.Generic;

public class MainClass
{
    static int[][] _tree;
    static int _lastValue = int.MinValue;    //константа, минимальное значение Int32
    
    public static void Main()
    {
        var n = int.Parse(Console.ReadLine());
        _tree = new int[n][];
        for(int i=0; i<n; i++)
            _tree[i] = Console.ReadLine().Split().Select(int.Parse).ToArray();
        
        Console.WriteLine(IsCorrect() ? "CORRECT" : "INCORRECT");    //тернарный условный оператор
    }
    
    static bool IsCorrect()
    {
        var stack = new Stack<int>();    //создаём стэк
        var i = 0;    //указывает на позицию вершины
        while(_tree.Length>0 && (i>=0 || stack.Count>0))    //пока дерево не закончится и число в стэке больше 0
        {
            //шагаем по веткам, до конца
            if(i > -1)    
            {
                stack.Push(i);   
                i = _tree[i][1];    
                continue;    
            }
            else
            {
                i = stack.Pop();
            }

            if(_lastValue >= _tree[i][0]) return false;    //сравниваем вершины
            _lastValue = _tree[i][0];
            i = _tree[i][2];
        }
        return true;
    }
}
