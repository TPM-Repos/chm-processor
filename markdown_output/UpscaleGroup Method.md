![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpscaleGroup Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5191.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : UpscaleGroup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_drivegroupStream_
    File stream to the drivegroup file that you wish to convert.

_groupName_
    The name of the group to upscale to - this can be different from the original group name.

_creationUsername_
    The server's admin username.

_creationPassword_
    The server's admin password.

Glossary Item Box

Converts the specified group into shared group that will be hosted by this server. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpscaleGroup( _
       ByVal _drivegroupStream_ As Stream, _
       ByVal _groupName_ As String, _
       ByVal _creationUsername_ As String, _
       ByVal _creationPassword_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupManager](topic5174.md)
    Dim drivegroupStream As Stream
    Dim groupName As String
    Dim creationUsername As String
    Dim creationPassword As String
     
    instance.UpscaleGroup(drivegroupStream, groupName, creationUsername, creationPassword)  
  
C#|   
---|---  
      
    
    public void UpscaleGroup( 
       Stream _drivegroupStream_ ,
       string _groupName_ ,
       string _creationUsername_ ,
       string _creationPassword_
    )  
  
#### Parameters

 _drivegroupStream_
    File stream to the drivegroup file that you wish to convert.
_groupName_
    The name of the group to upscale to - this can be different from the original group name.
_creationUsername_
    The server's admin username.
_creationPassword_
    The server's admin password.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)

©2024 DriveWorks Ltd. All Rights Reserved.
