Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskReleaseConditions Class](topic6682.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The zero-based index of the element to get.

Glossary Item Box

Gets the element at the specified index in the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ComponentTaskReleaseCondition](topic6647.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseConditions](topic6682.md)
    Dim index As Integer
    Dim value As [ComponentTaskReleaseCondition](topic6647.md)
     
    instance.Item(index) = value
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ComponentTaskReleaseCondition](topic6647.md) this[ 
       int _index_
    ]; {get; set;}  
  
#### Parameters

 _index_
    The zero-based index of the element to get.

#### Property Value

The element at the specified index in the read-only list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskReleaseConditions Class](topic6682.md)   
[ComponentTaskReleaseConditions Members](topic6683.md)


