![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EnsureTcpPortSharingServiceIsSetup Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5202.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupServer Class](topic5192.md) : EnsureTcpPortSharingServiceIsSetup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Enables pro server and its services to be hosted in more than one application at once. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub EnsureTcpPortSharingServiceIsSetup()   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupServer](topic5192.md)
     
    instance.EnsureTcpPortSharingServiceIsSetup()  
  
C#|   
---|---  
      
    
    public void EnsureTcpPortSharingServiceIsSetup()  
  
# ![](dotnetimages/collapse.gif)Remarks

This method attempts to find the "NetTcpPortSharing" service and start it (if it is not already running).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RemoteGroupServer Class](topic5192.md)   
[RemoteGroupServer Members](topic5193.md)

©2024 DriveWorks Ltd. All Rights Reserved.
