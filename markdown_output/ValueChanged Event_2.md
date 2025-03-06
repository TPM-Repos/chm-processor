       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValueChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4355.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDisplayFile Class](topic4346.md) : ValueChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines when the [Value](topic4354.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ValueChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDisplayFile](topic4346.md)
    Dim handler As EventHandler
     
    AddHandler instance.ValueChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler ValueChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDisplayFile Class](topic4346.md)   
[ProjectDisplayFile Members](topic4347.md)

©2024 DriveWorks Ltd. All Rights Reserved.
