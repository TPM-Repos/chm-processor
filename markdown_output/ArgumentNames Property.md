Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ArgumentNames Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) > [IFunctionInformation Interface](topic10512.md) : ArgumentNames Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Get the names of the arguments for the function, in order. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property ArgumentNames As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IFunctionInformation](topic10512.md)
    Dim value() As String
     
    value = instance.ArgumentNames  
  
C#|   
---|---  
      
    
    string[] ArgumentNames {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IFunctionInformation Interface](topic10512.md)   
[IFunctionInformation Members](topic10513.md)


