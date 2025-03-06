![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IAuthenticationProviderAsync Interface   
[Members](topic10583.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10582.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) : IAuthenticationProviderAsync Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for pluggable authentication systems in DriveWorks. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Interface IAuthenticationProviderAsync 
       Inherits [IAuthenticationProvider](topic10576.md)   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IAuthenticationProviderAsync](topic10582.md)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public interface IAuthenticationProviderAsync : [IAuthenticationProvider](topic10576.md)    
  
# ![](dotnetimages/collapse.gif)Remarks

In order for an instance of a type derived from this interface to be registered with the [AuthenticationProviderFactory](topic10617.md), the derived type must be marked with the [AuthenticationProviderNameAttribute](topic10626.md) attribute.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IAuthenticationProviderAsync Members](topic10583.md)   
[DriveWorks.Security Namespace](topic10574.md)

©2024 DriveWorks Ltd. All Rights Reserved.
