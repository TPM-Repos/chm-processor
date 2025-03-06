![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetParsedInput Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [FeatureContext Class](topic15189.md) : GetParsedInput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_inputName_
    The name of the input.

_valueIfMissing_
    A value to be returned if the value isn't present.

Glossary Item Box

Gets the parsed input with the given name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetParsedInput( _
       ByVal _inputName_ As String, _
       ByVal _valueIfMissing_ As Object _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FeatureContext](topic15189.md)
    Dim inputName As String
    Dim valueIfMissing As Object
    Dim value As Object
     
    value = instance.GetParsedInput(inputName, valueIfMissing)  
  
C#|   
---|---  
      
    
    public object GetParsedInput( 
       string _inputName_ ,
       object _valueIfMissing_
    )  
  
#### Parameters

 _inputName_
    The name of the input.
_valueIfMissing_
    A value to be returned if the value isn't present.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FeatureContext Class](topic15189.md)   
[FeatureContext Members](topic15190.md)


