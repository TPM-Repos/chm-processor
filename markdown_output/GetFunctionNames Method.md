Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetFunctionNames Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : GetFunctionNames Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns a list of supported callable functions for this project 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function GetFunctionNames() As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim value() As String
     
    value = instance.GetFunctionNames()  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public string[] GetFunctionNames()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


