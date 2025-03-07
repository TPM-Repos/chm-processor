Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetGroupConnectionInfo Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : GetGroupConnectionInfo Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupName_
    

Glossary Item Box

Gets information useful for connecting to a group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetGroupConnectionInfo( _
       ByVal _groupName_ As String _
    ) As [GroupConnectionInfo](topic3059.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupManager](topic5174.md)
    Dim groupName As String
    Dim value As [GroupConnectionInfo](topic3059.md)
     
    value = instance.GetGroupConnectionInfo(groupName)  
  
C#|   
---|---  
      
    
    public [GroupConnectionInfo](topic3059.md) GetGroupConnectionInfo( 
       string _groupName_
    )  
  
#### Parameters

 _groupName_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


