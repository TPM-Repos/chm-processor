Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationTaskList Class](topic11525.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_key_
    The key of the task list entry to retrieve.

Glossary Item Box

Gets the task list entry with the specified key. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _key_ As Object _
    ) As [SpecificationTaskListEntry](topic11537.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationTaskList](topic11525.md)
    Dim key As Object
    Dim value As [SpecificationTaskListEntry](topic11537.md)
     
    value = instance.Item(key)  
  
C#|   
---|---  
      
    
    public [SpecificationTaskListEntry](topic11537.md) this[ 
       object _key_
    ]; {get;}  
  
#### Parameters

 _key_
    The key of the task list entry to retrieve.

#### Property Value

The task list entry with the given key, or a null reference if one does not exist.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationTaskList Class](topic11525.md)   
[SpecificationTaskList Members](topic11526.md)


