Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskConditionNotFoundException Class   
[Members](topic7158.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) : ComponentTaskConditionNotFoundException Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an attempt is made to open a project that contains references to a [DriveWorks.Components.Tasks.ComponentTaskCondition](topic6493.md) or [DriveWorks.Components.Tasks.IComponentTaskCondition](topic6399.md) that are defined in an assembly that is not available. 

# Object Model

![](dotnetdiagramimages/image384.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <SerializableAttribute()>
    Public Class ComponentTaskConditionNotFoundException 
       Inherits System.Exception  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditionNotFoundException](topic7157.md)  
  
C#|   
---|---  
      
    
    [SerializableAttribute()]
    public class ComponentTaskConditionNotFoundException : System.Exception   
  
# Inheritance Hierarchy

System.Object  
System.Exception  
**DriveWorks.Extensibility.ComponentTaskConditionNotFoundException**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskConditionNotFoundException Members](topic7158.md)   
[DriveWorks.Extensibility Namespace](topic7150.md)


