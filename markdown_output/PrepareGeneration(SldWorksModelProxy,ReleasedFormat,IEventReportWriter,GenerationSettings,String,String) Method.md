![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PrepareGeneration(SldWorksModelProxy,ReleasedFormat,IEventReportWriter,GenerationSettings,String,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13590.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) > [PrepareGeneration Method](topic13588.md) : PrepareGeneration(SldWorksModelProxy,ReleasedFormat,IEventReportWriter,GenerationSettings,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_model_
    The from which the file will be created.

_format_
    The released format information to use during generation.

_report_
    The report to use for any generation issues etc.

_settings_
    The generation settings to use during generation.

_modelPath_
    The path of the component to create the format from.

_tempDirectory_
    The temporary directory to use during generation.

Glossary Item Box

Called before main generation, should be used to initialize and evaluate parameters to determine if generation can take place. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overridable Function PrepareGeneration( _
       ByVal _model_ As SldWorksModelProxy, _
       ByVal _format_ As [ReleasedFormat](topic14925.md), _
       ByVal _report_ As [IEventReportWriter](topic10336.md), _
       ByVal _settings_ As [GenerationSettings](topic15238.md), _
       ByVal _modelPath_ As String, _
       ByVal _tempDirectory_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim model As SldWorksModelProxy
    Dim format As [ReleasedFormat](topic14925.md)
    Dim report As [IEventReportWriter](topic10336.md)
    Dim settings As [GenerationSettings](topic15238.md)
    Dim modelPath As String
    Dim tempDirectory As String
    Dim value As Boolean
     
    value = instance.PrepareGeneration(model, format, report, settings, modelPath, tempDirectory)  
  
C#|   
---|---  
      
    
    public virtual bool PrepareGeneration( 
       SldWorksModelProxy _model_ ,
       [ReleasedFormat](topic14925.md) _format_ ,
       [IEventReportWriter](topic10336.md) _report_ ,
       [GenerationSettings](topic15238.md) _settings_ ,
       string _modelPath_ ,
       string _tempDirectory_
    )  
  
#### Parameters

 _model_
    The from which the file will be created.
_format_
    The released format information to use during generation.
_report_
    The report to use for any generation issues etc.
_settings_
    The generation settings to use during generation.
_modelPath_
    The path of the component to create the format from.
_tempDirectory_
    The temporary directory to use during generation.

#### Return Value

Whether or not generation is possible.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)   
[Overload List](topic13588.md)

©2024 DriveWorks Ltd. All Rights Reserved.
