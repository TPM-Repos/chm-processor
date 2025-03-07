Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MasterPath Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectSolidWorksComponent Class](topic14692.md) : MasterPath Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the master path for the component if the capture data is resolved, otherwise throws an exception. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property MasterPath As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSolidWorksComponent](topic14692.md)
    Dim value As String
     
    value = instance.MasterPath  
  
C#|   
---|---  
      
    
    public string MasterPath {get;}  
  
# Exceptions

Exception| Description  
---|---  
**DriveWorks.Components.Data.NotResolvedException**|  The capture data is not resolved.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSolidWorksComponent Class](topic14692.md)   
[ProjectSolidWorksComponent Members](topic14693.md)


