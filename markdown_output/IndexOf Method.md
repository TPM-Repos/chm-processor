Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IndexOf Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Conditions Class](topic10865.md) : IndexOf Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_condition_
    The condition whose index to retrieve.

Glossary Item Box

Gets the index of the given condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IndexOf( _
       ByVal _condition_ As [Condition](topic10804.md) _
    ) As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Conditions](topic10865.md)
    Dim condition As [Condition](topic10804.md)
    Dim value As Integer
     
    value = instance.IndexOf(condition)  
  
C#|   
---|---  
      
    
    public int IndexOf( 
       [Condition](topic10804.md) _condition_
    )  
  
#### Parameters

 _condition_
    The condition whose index to retrieve.

#### Return Value

The index of the condition, or -1 if the condition is not a part of this collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Conditions Class](topic10865.md)   
[Conditions Members](topic10866.md)


