![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetGroupConnectionInfo Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5187.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : GetGroupConnectionInfo Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupName_
    

Glossary Item Box

Gets information useful for connecting to a group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetGroupConnectionInfo( _
       ByVal _groupName_ As String _
    ) As [GroupConnectionInfo](topic3059.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)

©2024 DriveWorks Ltd. All Rights Reserved.
