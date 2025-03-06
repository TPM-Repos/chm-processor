UpscaleGroup Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpscaleGroup( _
       ByVal _drivegroupStream_ As Stream, _
       ByVal _groupName_ As String, _
       ByVal _creationUsername_ As String, _
       ByVal _creationPassword_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


