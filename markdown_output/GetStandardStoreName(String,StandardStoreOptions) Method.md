![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetStandardStoreName(String,StandardStoreOptions) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9414.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) > [GetStandardStoreName Method](topic9412.md) : GetStandardStoreName(String,StandardStoreOptions) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlName_
    The name of the control that has the store option.

_opt_
    The standard store option to get the reference for.

Glossary Item Box

Gets the reference name that will be used for the specified control name and store option combination. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function GetStandardStoreName( _
       ByVal _controlName_ As String, _
       ByVal _opt_ As [StandardStoreOptions](topic9384.md) _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim controlName As String
    Dim opt As [StandardStoreOptions](topic9384.md)
    Dim value As String
     
    value = [DynamicProperty](topic9398.md).GetStandardStoreName(controlName, opt)  
  
C#|   
---|---  
      
    
    public static string GetStandardStoreName( 
       string _controlName_ ,
       [StandardStoreOptions](topic9384.md) _opt_
    )  
  
#### Parameters

 _controlName_
    The name of the control that has the store option.
_opt_
    The standard store option to get the reference for.

#### Return Value

Returns the store name for the specified combination, else throws an exception.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| Thrown when unknown opt value is given.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)   
[Overload List](topic9412.md)

©2024 DriveWorks Ltd. All Rights Reserved.
