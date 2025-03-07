Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateFunctionInvariant Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Localization Namespace](topic10015.md) > [RuleLocalizationHelper Class](topic10018.md) : CreateFunctionInvariant Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_functionName_
    The function name.

_arguments_
    The arguments to be passed to the function.

Glossary Item Box

Creates a function call without localizing the function name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateFunctionInvariant( _
       ByVal _functionName_ As String, _
       ByVal ParamArray _arguments_() As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleLocalizationHelper](topic10018.md)
    Dim functionName As String
    Dim arguments() As String
    Dim value As String
     
    value = instance.CreateFunctionInvariant(functionName, arguments)  
  
C#|   
---|---  
      
    
    public string CreateFunctionInvariant( 
       string _functionName_ ,
       params string[] _arguments_
    )  
  
#### Parameters

 _functionName_
    The function name.
_arguments_
    The arguments to be passed to the function.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleLocalizationHelper Class](topic10018.md)   
[RuleLocalizationHelper Members](topic10019.md)


