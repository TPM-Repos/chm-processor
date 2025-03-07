Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopyTo Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskReleaseConditions Class](topic6682.md) : CopyTo Method  
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
       ByVal _array_() As [ComponentTaskReleaseCondition](topic6647.md), _
       ByVal _arrayIndex_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseConditions](topic6682.md)
    Dim array() As [ComponentTaskReleaseCondition](topic6647.md)
    Dim arrayIndex As Integer
     
    instance.CopyTo(array, arrayIndex)  
  
C#|   
---|---  
      
    
    public void CopyTo( 
       [ComponentTaskReleaseCondition](topic6647.md)[] _array_ ,
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

[ComponentTaskReleaseConditions Class](topic6682.md)   
[ComponentTaskReleaseConditions Members](topic6683.md)


