       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Started Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1847.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ConnectorBase Class](topic1834.md) : Started Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a connector has started. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event Started As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectorBase](topic1834.md)
    Dim handler As EventHandler
     
    AddHandler instance.Started, handler  
  
C#|   
---|---  
      
    
    public event EventHandler Started  
  
# Remarks

Implementors should raise this event when the connector is started by the [Start](topic1702.md) method. A connector should never start itself.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectorBase Class](topic1834.md)   
[ConnectorBase Members](topic1835.md)

©2024 DriveWorks Ltd. All Rights Reserved.
