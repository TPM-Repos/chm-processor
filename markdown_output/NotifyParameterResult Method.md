![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyParameterResult Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6118.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseParameterTracker Interface](topic6113.md) : NotifyParameterResult Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_parameterTypeName_
    The invariant name of the parameter's type.

_parameterTypeDisplayName_
    The display name of the parameter's type.

_parameterName_
    The display name of the parameter.

_parameterRule_
    The rule which was used to calculate the parameter's result.

_parameterResult_
    The result of calculating the parameter's rule.

Glossary Item Box

Called when a parameter result is finalized. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyParameterResult( _
       ByVal _parameterTypeName_ As String, _
       ByVal _parameterTypeDisplayName_ As String, _
       ByVal _parameterName_ As String, _
       ByVal _parameterRule_ As String, _
       ByVal _parameterResult_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReleaseParameterTracker](topic6113.md)
    Dim parameterTypeName As String
    Dim parameterTypeDisplayName As String
    Dim parameterName As String
    Dim parameterRule As String
    Dim parameterResult As String
     
    instance.NotifyParameterResult(parameterTypeName, parameterTypeDisplayName, parameterName, parameterRule, parameterResult)  
  
C#|   
---|---  
      
    
    void NotifyParameterResult( 
       string _parameterTypeName_ ,
       string _parameterTypeDisplayName_ ,
       string _parameterName_ ,
       string _parameterRule_ ,
       string _parameterResult_
    )  
  
#### Parameters

 _parameterTypeName_
    The invariant name of the parameter's type.
_parameterTypeDisplayName_
    The display name of the parameter's type.
_parameterName_
    The display name of the parameter.
_parameterRule_
    The rule which was used to calculate the parameter's result.
_parameterResult_
    The result of calculating the parameter's rule.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleaseParameterTracker Interface](topic6113.md)   
[IReleaseParameterTracker Members](topic6114.md)

©2024 DriveWorks Ltd. All Rights Reserved.
