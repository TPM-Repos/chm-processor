![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PollingConnectorBase Class   
[Members](topic1915.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1914.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : PollingConnectorBase Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a base class for connectors which use a polling strategy. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image66.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class PollingConnectorBase 
       Inherits [ConnectorBase](topic1834.md)
       Implements [IConnector](topic1697.md), [DriveWorks.Applications.Extensibility.IApplicationPlugin](topic2004.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [PollingConnectorBase](topic1914.md)  
  
C#|   
---|---  
      
    
    public abstract class PollingConnectorBase : [ConnectorBase](topic1834.md), [IConnector](topic1697.md), [DriveWorks.Applications.Extensibility.IApplicationPlugin](topic2004.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
[DriveWorks.Applications.Autopilot.Extensibility.ConnectorBase](topic1834.md)  
**DriveWorks.Applications.Autopilot.Extensibility.PollingConnectorBase**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PollingConnectorBase Members](topic1915.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)

©2024 DriveWorks Ltd. All Rights Reserved.
