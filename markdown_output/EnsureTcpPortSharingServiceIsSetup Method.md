Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EnsureTcpPortSharingServiceIsSetup Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupServer Class](topic5192.md) : EnsureTcpPortSharingServiceIsSetup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Enables pro server and its services to be hosted in more than one application at once. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub EnsureTcpPortSharingServiceIsSetup()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupServer](topic5192.md)
     
    instance.EnsureTcpPortSharingServiceIsSetup()  
  
C#|   
---|---  
      
    
    public void EnsureTcpPortSharingServiceIsSetup()  
  
# Remarks

This method attempts to find the "NetTcpPortSharing" service and start it (if it is not already running).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupServer Class](topic5192.md)   
[RemoteGroupServer Members](topic5193.md)


