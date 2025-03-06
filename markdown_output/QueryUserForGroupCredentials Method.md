![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueryUserForGroupCredentials Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic249.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupCredentialsProvider Interface](topic244.md) : QueryUserForGroupCredentials Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    Information about the credentials request.

Glossary Item Box

Requests credentials from the user to be used to log on to the group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function QueryUserForGroupCredentials( _
       ByVal _context_ As [GroupCredentialsRequestContext](topic835.md) _
    ) As [IProviderCredentials](topic10588.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IGroupCredentialsProvider](topic244.md)
    Dim context As [GroupCredentialsRequestContext](topic835.md)
    Dim value As [IProviderCredentials](topic10588.md)
     
    value = instance.QueryUserForGroupCredentials(context)  
  
C#|   
---|---  
      
    
    [IProviderCredentials](topic10588.md) QueryUserForGroupCredentials( 
       [GroupCredentialsRequestContext](topic835.md) _context_
    )  
  
#### Parameters

 _context_
    Information about the credentials request.

#### Return Value

A credentials object which can be passed to the Group open method to log on to the group.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IGroupCredentialsProvider Interface](topic244.md)   
[IGroupCredentialsProvider Members](topic245.md)

©2024 DriveWorks Ltd. All Rights Reserved.
