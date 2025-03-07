Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerateCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupTableExport Class](topic3414.md) : GenerateCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_generateDirectory_
    

_results_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub GenerateCore( _
       ByVal _generateDirectory_ As String, _
       ByVal _results_ As [RuleResults](topic11136.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupTableExport](topic3414.md)
    Dim generateDirectory As String
    Dim results As [RuleResults](topic11136.md)
     
    instance.GenerateCore(generateDirectory, results)  
  
C#|   
---|---  
      
    
    protected override void GenerateCore( 
       string _generateDirectory_ ,
       [RuleResults](topic11136.md) _results_
    )  
  
#### Parameters

 _generateDirectory_
    
_results_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupTableExport Class](topic3414.md)   
[GroupTableExport Members](topic3415.md)


