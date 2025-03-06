![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationPluginAttribute Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2112.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ApplicationPluginAttribute Class](topic2106.md) : ApplicationPluginAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The invariant name of the plugin.

_displayName_
    The localized display name of the plugin.

_description_
    The localized description of the plugin.

Glossary Item Box

Initializes a new instance of the [ApplicationPluginAttribute](topic2106.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _name_ As String, _
       ByVal _displayName_ As String, _
       ByVal _description_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim name As String
    Dim displayName As String
    Dim description As String
     
    Dim instance As New [ApplicationPluginAttribute](topic2106.md)(name, displayName, description)  
  
C#|   
---|---  
      
    
    public ApplicationPluginAttribute( 
       string _name_ ,
       string _displayName_ ,
       string _description_
    )  
  
#### Parameters

 _name_
    The invariant name of the plugin.
_displayName_
    The localized display name of the plugin.
_description_
    The localized description of the plugin.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ApplicationPluginAttribute Class](topic2106.md)   
[ApplicationPluginAttribute Members](topic2107.md)

©2024 DriveWorks Ltd. All Rights Reserved.
