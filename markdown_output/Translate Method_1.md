![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Translate Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1806.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ITranslator Interface](topic1801.md) : Translate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_request_
    The raw data to be translated.

Glossary Item Box

Translates the specified raw data into a series of instances of [ISpecificationRequest](topic1778.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function Translate( _
       ByVal _request_ As [ITranslationRequest](topic1791.md) _
    ) As [ISpecificationRequest()](topic1778.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ITranslator](topic1801.md)
    Dim request As [ITranslationRequest](topic1791.md)
    Dim value() As [ISpecificationRequest](topic1778.md)
     
    value = instance.Translate(request)  
  
C#|   
---|---  
      
    
    [ISpecificationRequest[]](topic1778.md) Translate( 
       [ITranslationRequest](topic1791.md) _request_
    )  
  
#### Parameters

 _request_
    The raw data to be translated.

#### Return Value

An array of instances of [ISpecificationRequest](topic1778.md) if the raw data was successfully translated, otherwise a null reference (Nothing in Visual Basic).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ITranslator Interface](topic1801.md)   
[ITranslator Members](topic1802.md)

©2024 DriveWorks Ltd. All Rights Reserved.
