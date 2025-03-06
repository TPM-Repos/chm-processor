![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IListPropertyEditor Interface   
[Members](topic1292.md) Example See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1291.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility Namespace](topic1277.md) : IListPropertyEditor Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for a **IPropertyEditor** class that signals that DriveWorks should use inline dropdown property behaviour instead of the **IPropertyEditor.EditValue** method to edit the property's value. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Interface IListPropertyEditor 
       Inherits [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IListPropertyEditor](topic1291.md)  
  
C#|   
---|---  
      
    
    public interface IListPropertyEditor : [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# ![](dotnetimages/collapse.gif)Example

C#| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    //Import main DriveWorks types
    [PropertyEditor("RuleType.ColorOptions")]
    public class ColorOptionEditor : IListPropertyEditor
    {
    	public string CommandTitle => "Color options editor";
                
        public Image CommandImage => null/* TODO Change to default(_) if this is not a reference type */;
                
        public UITypeEditorEditStyle EditorStyle => UITypeEditorEditStyle.DropDown;
                
        public void Initialize(IApplication application)
        {
        }
                
        public string EditValue(IPropertyContext context)
        {
            return context.CurrentValueAsString; // Not relevant to list editors
        }
                
        public string EditValueInDialog(IPropertyContext context)
        {
            return context.CurrentValueAsString; // Not relevant to list editors
        }
                
        public IEnumerable<string> GetItems()
        {
            return Enum.GetNames(typeof(ColorOptions));
        }
                
        private enum ColorOptions
        {
            Red,
            Blue,
            Green
        }
    }  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IListPropertyEditor Members](topic1292.md)   
[DriveWorks.Applications.Administrator.Extensibility Namespace](topic1277.md)

©2024 DriveWorks Ltd. All Rights Reserved.
