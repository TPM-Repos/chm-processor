Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExcludedStates Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [StateFilter Class](topic1077.md) : ExcludedStates Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the states from which the entity controlled by the filter is excluded. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ExcludedStates As Guid()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StateFilter](topic1077.md)
    Dim value() As Guid
     
    value = instance.ExcludedStates  
  
C#|   
---|---  
      
    
    public Guid[] ExcludedStates {get;}  
  
#### Property Value

An array of globally unique identifiers representing the individual states from which to exclude the filtered entity.

# Remarks

To prevent modification, the result array is cloned each time this property is accessed, if frequent accesses are made to this property, consider caching the result.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StateFilter Class](topic1077.md)   
[StateFilter Members](topic1078.md)


