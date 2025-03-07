Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IncludedStates Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [StateFilter Class](topic1077.md) : IncludedStates Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the states in which the entity controlled by the filter is included. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IncludedStates As Guid()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StateFilter](topic1077.md)
    Dim value() As Guid
     
    value = instance.IncludedStates  
  
C#|   
---|---  
      
    
    public Guid[] IncludedStates {get;}  
  
#### Property Value

An array of globally unique identifiers representing the individual states in which to include the filtered entity.

# Remarks

To prevent modification, the result array is cloned each time this property is access, if frequent accesses are made to this property, consider caching the result.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StateFilter Class](topic1077.md)   
[StateFilter Members](topic1078.md)


