Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Contains Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskReleaseConditions Class](topic6682.md) : Contains Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_condition_
    The condition to locate in the collection.

Glossary Item Box

Determines whether the collection contains a specific condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Contains( _
       ByVal _condition_ As [ComponentTaskReleaseCondition](topic6647.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseConditions](topic6682.md)
    Dim condition As [ComponentTaskReleaseCondition](topic6647.md)
    Dim value As Boolean
     
    value = instance.Contains(condition)  
  
C#|   
---|---  
      
    
    public bool Contains( 
       [ComponentTaskReleaseCondition](topic6647.md) _condition_
    )  
  
#### Parameters

 _condition_
    The condition to locate in the collection.

#### Return Value

True if the condition was found in the collection, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskReleaseConditions Class](topic6682.md)   
[ComponentTaskReleaseConditions Members](topic6683.md)


