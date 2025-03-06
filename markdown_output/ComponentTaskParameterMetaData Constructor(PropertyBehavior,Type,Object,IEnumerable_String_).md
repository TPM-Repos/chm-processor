![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskParameterMetaData Constructor(PropertyBehavior,Type,Object,IEnumerable<String>)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6628.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskParameterMetaData Class](topic6619.md) > [ComponentTaskParameterMetaData Constructor](topic6625.md) : ComponentTaskParameterMetaData Constructor(PropertyBehavior,Type,Object,IEnumerable<String>)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_behaviour_
    The behavior of the property.

_valueType_
    The CLR type of the property when it is static (if supported).

_defaultValue_
    The default value of the property when it has just been created.

_ruleTypes_
    The rule type of the [ComponentTaskProperty](topic6633.md).

Glossary Item Box

Creates a new instance of the [ComponentTaskParameterMetaData](topic6619.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _behaviour_ As [PropertyBehavior](topic9383.md), _
       ByVal _valueType_ As Type, _
       ByVal _defaultValue_ As Object, _
       ByVal _ruleTypes_ As IEnumerable(Of String) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim behaviour As [PropertyBehavior](topic9383.md)
    Dim valueType As Type
    Dim defaultValue As Object
    Dim ruleTypes As IEnumerable(Of String)
     
    Dim instance As New [ComponentTaskParameterMetaData](topic6619.md)(behaviour, valueType, defaultValue, ruleTypes)  
  
C#|   
---|---  
      
    
    public ComponentTaskParameterMetaData( 
       [PropertyBehavior](topic9383.md) _behaviour_ ,
       Type _valueType_ ,
       object _defaultValue_ ,
       IEnumerable<string> _ruleTypes_
    )  
  
#### Parameters

 _behaviour_
    The behavior of the property.
_valueType_
    The CLR type of the property when it is static (if supported).
_defaultValue_
    The default value of the property when it has just been created.
_ruleTypes_
    The rule type of the [ComponentTaskProperty](topic6633.md).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskParameterMetaData Class](topic6619.md)   
[ComponentTaskParameterMetaData Members](topic6620.md)   
[Overload List](topic6625.md)

©2024 DriveWorks Ltd. All Rights Reserved.
