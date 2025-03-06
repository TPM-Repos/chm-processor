![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProperties(Type,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) > [GetProperties Method](topic9409.md) : GetProperties(Type,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlType_
    

_excludeHiddenProperties_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function GetProperties( _
       ByVal _controlType_ As Type, _
       ByVal _excludeHiddenProperties_ As Boolean _
    ) As [DynamicProperty()](topic9398.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim controlType As Type
    Dim excludeHiddenProperties As Boolean
    Dim value() As [DynamicProperty](topic9398.md)
     
    value = [DynamicProperty](topic9398.md).GetProperties(controlType, excludeHiddenProperties)  
  
C#|   
---|---  
      
    
    public static [DynamicProperty[]](topic9398.md) GetProperties( 
       Type _controlType_ ,
       bool _excludeHiddenProperties_
    )  
  
#### Parameters

 _controlType_
    
_excludeHiddenProperties_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)   
[Overload List](topic9409.md)


