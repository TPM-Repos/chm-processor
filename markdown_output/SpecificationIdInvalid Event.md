       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationIdInvalid Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic487.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISpecificationRequestWithEdit Interface](topic478.md) : SpecificationIdInvalid Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when the specification is being edited and a specification with the given name can't be located. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event SpecificationIdInvalid As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationRequestWithEdit](topic478.md)
    Dim handler As EventHandler
     
    AddHandler instance.SpecificationIdInvalid, handler  
  
C#|   
---|---  
      
    
    event EventHandler SpecificationIdInvalid  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationRequestWithEdit Interface](topic478.md)   
[ISpecificationRequestWithEdit Members](topic479.md)

©2024 DriveWorks Ltd. All Rights Reserved.
