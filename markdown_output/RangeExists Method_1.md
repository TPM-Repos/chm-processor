Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RangeExists Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [WordDocument Class](topic5885.md) : RangeExists Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rangeName_
    Name of the driven bookmark to find the existence of.

Glossary Item Box

Sees if a given driven bookmark exists with a specific name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RangeExists( _
       ByVal _rangeName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WordDocument](topic5885.md)
    Dim rangeName As String
    Dim value As Boolean
     
    value = instance.RangeExists(rangeName)  
  
C#|   
---|---  
      
    
    public bool RangeExists( 
       string _rangeName_
    )  
  
#### Parameters

 _rangeName_
    Name of the driven bookmark to find the existence of.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WordDocument Class](topic5885.md)   
[WordDocument Members](topic5886.md)


