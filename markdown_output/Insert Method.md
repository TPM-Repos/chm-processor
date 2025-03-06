![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Insert Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Conditions Class](topic10865.md) : Insert Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index at which to insert the condition.

_condition_
    The condition to insert.

Glossary Item Box

Inserts the condition into the condition sequence at the specified index. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Insert( _
       ByVal _index_ As Integer, _
       ByVal _condition_ As [Condition](topic10804.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Conditions](topic10865.md)
    Dim index As Integer
    Dim condition As [Condition](topic10804.md)
     
    instance.Insert(index, condition)  
  
C#|   
---|---  
      
    
    public void Insert( 
       int _index_ ,
       [Condition](topic10804.md) _condition_
    )  
  
#### Parameters

 _index_
    The index at which to insert the condition.
_condition_
    The condition to insert.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.IndexOutOfRangeException| Thrown if the index parameter is out of range.  
System.ArgumentNullException| Thrown if the condition parameter is a null reference.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Conditions Class](topic10865.md)   
[Conditions Members](topic10866.md)


