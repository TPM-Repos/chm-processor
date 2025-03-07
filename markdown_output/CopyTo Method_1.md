Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub CopyTo( _
       ByVal _array_() As [ComponentTaskCondition](topic6493.md), _
       ByVal _arrayIndex_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskConditions Class](topic6561.md)   
[ComponentTaskConditions Members](topic6562.md)


