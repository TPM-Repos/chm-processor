Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCanExecute Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [RemapComponentsAction Class](topic9949.md) : GetCanExecute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_useCache_
    Whether or not he value needs to be re-evaluated from a last attempt.

Glossary Item Box

Checks to see if the action can be executed or not. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function GetCanExecute( _
       ByVal _useCache_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemapComponentsAction](topic9949.md)
    Dim useCache As Boolean
    Dim value As Boolean
     
    value = instance.GetCanExecute(useCache)  
  
C#|   
---|---  
      
    
    public override bool GetCanExecute( 
       bool _useCache_
    )  
  
#### Parameters

 _useCache_
    Whether or not he value needs to be re-evaluated from a last attempt.

#### Return Value

True if it can execute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemapComponentsAction Class](topic9949.md)   
[RemapComponentsAction Members](topic9950.md)


