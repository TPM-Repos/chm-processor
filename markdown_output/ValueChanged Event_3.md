       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValueChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4781.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecialVariable Class](topic4762.md) : ValueChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever the value of the Special Variable changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ValueChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecialVariable](topic4762.md)
    Dim handler As EventHandler
     
    AddHandler instance.ValueChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler ValueChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecialVariable Class](topic4762.md)   
[ProjectSpecialVariable Members](topic4763.md)

©2024 DriveWorks Ltd. All Rights Reserved.
