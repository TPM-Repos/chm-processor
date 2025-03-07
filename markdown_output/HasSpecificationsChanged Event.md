Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HasSpecificationsChanged Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISpecificationsManager Interface](topic13440.md) : HasSpecificationsChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the value of the [HasSpecifications](topic13447.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event HasSpecificationsChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationsManager](topic13440.md)
    Dim handler As EventHandler
     
    AddHandler instance.HasSpecificationsChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler HasSpecificationsChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationsManager Interface](topic13440.md)   
[ISpecificationsManager Members](topic13441.md)


