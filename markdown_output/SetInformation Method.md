![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetInformation Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1713.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IGroupConnector Interface](topic1706.md) : SetInformation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The new group connect details for this connector.

Glossary Item Box

Used to inform this connector of it's connector details. This will be called after connector creation and whenever the details are updated. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetInformation( _
       ByVal _info_ As [GroupConnectorInformation](topic3084.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IGroupConnector](topic1706.md)
    Dim info As [GroupConnectorInformation](topic3084.md)
     
    instance.SetInformation(info)  
  
C#|   
---|---  
      
    
    void SetInformation( 
       [GroupConnectorInformation](topic3084.md) _info_
    )  
  
#### Parameters

 _info_
    The new group connect details for this connector.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IGroupConnector Interface](topic1706.md)   
[IGroupConnector Members](topic1707.md)

©2024 DriveWorks Ltd. All Rights Reserved.
