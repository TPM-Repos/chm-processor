![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OpenGroup Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupService Interface](topic251.md) : OpenGroup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupConnectionString_
    The connection string which describes the group to which to connect.

_groupCredentials_
    The credentials to use to connect to the group, or a null rereference to prompt the user for credentials if the implementation supports it.

Glossary Item Box

Opens the specified group with the given credentials. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub OpenGroup( _
       ByVal _groupConnectionString_ As String, _
       ByVal _groupCredentials_ As [IProviderCredentials](topic10588.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IGroupService](topic251.md)
    Dim groupConnectionString As String
    Dim groupCredentials As [IProviderCredentials](topic10588.md)
     
    instance.OpenGroup(groupConnectionString, groupCredentials)  
  
C#|   
---|---  
      
    
    void OpenGroup( 
       string _groupConnectionString_ ,
       [IProviderCredentials](topic10588.md) _groupCredentials_
    )  
  
#### Parameters

 _groupConnectionString_
    The connection string which describes the group to which to connect.
_groupCredentials_
    The credentials to use to connect to the group, or a null rereference to prompt the user for credentials if the implementation supports it.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The implementation does not support groups being opened by 3rd party code.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IGroupService Interface](topic251.md)   
[IGroupService Members](topic252.md)


