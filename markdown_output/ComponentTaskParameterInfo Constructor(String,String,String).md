![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskParameterInfo Constructor(String,String,String)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6611.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskParameterInfo Class](topic6603.md) > [ComponentTaskParameterInfo Constructor](topic6609.md) : ComponentTaskParameterInfo Constructor(String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter.

_displayName_
    The name of the parameter to show end end user.

_description_
    The description of the parameter.

Glossary Item Box

Creates a new instance of the [ComponentTaskParameterInfo](topic6603.md) class. 

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
     
    Dim instance As New [ComponentTaskParameterInfo](topic6603.md)(name, displayName, description)  
  
C#|   
---|---  
      
    
    public ComponentTaskParameterInfo( 
       string _name_ ,
       string _displayName_ ,
       string _description_
    )  
  
#### Parameters

 _name_
    The name of the parameter.
_displayName_
    The name of the parameter to show end end user.
_description_
    The description of the parameter.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentException| name is null or empty.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskParameterInfo Class](topic6603.md)   
[ComponentTaskParameterInfo Members](topic6604.md)   
[Overload List](topic6609.md)

©2024 DriveWorks Ltd. All Rights Reserved.
