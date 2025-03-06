       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic306.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IHasState Interface](topic300.md) : StateChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the current state of the object changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event StateChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasState](topic300.md)
    Dim handler As EventHandler
     
    AddHandler instance.StateChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler StateChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasState Interface](topic300.md)   
[IHasState Members](topic301.md)

©2024 DriveWorks Ltd. All Rights Reserved.
