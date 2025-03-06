       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRange(String,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5903.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [WordDocument Class](topic5885.md) > [SetRange Method](topic5902.md) : SetRange(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    Name of the range to be driven.

_formula_
    Formula of the range.

Glossary Item Box

Sets/adds a bookmark to be driven. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub SetRange( _
       ByVal _name_ As String, _
       ByVal _formula_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WordDocument](topic5885.md)
    Dim name As String
    Dim formula As String
     
    instance.SetRange(name, formula)  
  
C#|   
---|---  
      
    
    public void SetRange( 
       string _name_ ,
       string _formula_
    )  
  
#### Parameters

 _name_
    Name of the range to be driven.
_formula_
    Formula of the range.

# Remarks

A name must exactly equal Word file's range name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WordDocument Class](topic5885.md)   
[WordDocument Members](topic5886.md)   
[Overload List](topic5902.md)

©2024 DriveWorks Ltd. All Rights Reserved.
