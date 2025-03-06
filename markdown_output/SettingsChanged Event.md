       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SettingsChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic231.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IFormDesignerProjectSettings Interface](topic215.md) : SettingsChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever any setting values have been changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event SettingsChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IFormDesignerProjectSettings](topic215.md)
    Dim handler As EventHandler
     
    AddHandler instance.SettingsChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler SettingsChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IFormDesignerProjectSettings Interface](topic215.md)   
[IFormDesignerProjectSettings Members](topic216.md)

©2024 DriveWorks Ltd. All Rights Reserved.
