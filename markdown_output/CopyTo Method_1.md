![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopyTo Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditions Class](topic6561.md) : CopyTo Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_array_
    The one-dimensional System.Array that is the destination of the elements copied from this collection.

_arrayIndex_
    The zero-based index in array at which copying begins.

Glossary Item Box

Copies the elements of the System.Collections.Generic.ICollection`1 to an System.Array, starting at a particular System.Array index. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub CopyTo( _
       ByVal _array_() As [ComponentTaskCondition](topic6493.md), _
       ByVal _arrayIndex_ As Integer _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditions](topic6561.md)
    Dim array() As [ComponentTaskCondition](topic6493.md)
    Dim arrayIndex As Integer
     
    instance.CopyTo(array, arrayIndex)  
  
C#|   
---|---  
      
    
    public void CopyTo( 
       [ComponentTaskCondition](topic6493.md)[] _array_ ,
       int _arrayIndex_
    )  
  
#### Parameters

 _array_
    The one-dimensional System.Array that is the destination of the elements copied from this collection.
_arrayIndex_
    The zero-based index in array at which copying begins.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskConditions Class](topic6561.md)   
[ComponentTaskConditions Members](topic6562.md)


