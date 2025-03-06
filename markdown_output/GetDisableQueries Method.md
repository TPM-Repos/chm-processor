![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetDisableQueries Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [Extensions Class](topic814.md) : GetDisableQueries Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_this_
    

Glossary Item Box

Gets the value of the Disable Queries setting. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <ExtensionAttribute()>
    Public Shared Function GetDisableQueries( _
       ByVal _this_ As [ISettingsManager](topic442.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim this As [ISettingsManager](topic442.md)
    Dim value As Boolean
     
    value = [Extensions](topic814.md).GetDisableQueries(this)  
  
C#|   
---|---  
      
    
    [ExtensionAttribute()]
    public static bool GetDisableQueries( 
       [ISettingsManager](topic442.md) _this_
    )  
  
#### Parameters

 _this_
    

#### Return Value

The value of the Disable Queries setting.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Extensions Class](topic814.md)   
[Extensions Members](topic815.md)


